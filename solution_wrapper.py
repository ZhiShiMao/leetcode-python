from types import FunctionType
from typing import Dict, Optional


def solution_wrapper(cls):
    def to_cases() -> Dict:
        """获取Solution类__doc__中的测试用例

        返回类似结构：
        [
            {
                "params": {"nums": [2, 7, 11, 15], "target": 9},
                "results": [0, 1],
            },
            {
                "params": {"nums": [3, 2, 4], "target": 6},
                "results": [1, 2],
            },
            {
                "params": {"nums": [3, 3], "target": 6},
                "results": [0, 1],
            },
        ]

        Returns:
            Dict: 返回所有的测试用例
        """
        lines = cls.__doc__.split("\n")
        test_cases = []
        for line in lines:
            index = line.find("输入：")
            if index >= 0:
                test_case = {"params": {}, "results": None}
                params = line[index + 3 :].split(", ")
                for param in params:
                    param = param.split("=")
                    key = param[0].strip()
                    value = param[1].strip()
                    test_case["params"][key] = eval(value)
                test_cases.append(test_case)

            index = line.find("输出：")
            if index >= 0:
                results = line[index + 3 :]
                test_case["results"] = eval(results)
        return test_cases

    def find_func() -> Optional[str]:
        """获取Solution中算法函数名称

        Returns:
            Optional[str]: 返回函数名称
        """
        for key, value in vars(cls).items():
            if not key.startswith("__"):
                return value.__name__
        return None

    def wrapper(*args, **kwargs) -> FunctionType:
        """生成Solution类型的实例化函数

        Returns:
            FunctionType: 返回生成Solution类型的实例化函数
        """

        obj = cls(*args, **kwargs)
        func_name = find_func()
        for test_case in to_cases():
            results = eval(f"obj.{func_name}")(**test_case["params"])
            except_results = test_case["results"]
            print(results, except_results)
        return obj

    return wrapper
