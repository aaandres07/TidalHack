from dataclasses import dataclass
from typing import Dict

@dataclass
class ClassInfo:
    rooms: Dict[str, int]

@dataclass
class DegreePlan:
    name: str
    classes: Dict[str, ClassInfo]

def get_degree_class_data():
    MEEN = DegreePlan(
        name="MEEN",
        classes={
            "CHEM 107": ClassInfo(rooms={"ILCB": 50}),
            "CHEM 117": ClassInfo(rooms={"HELD": 50}),
            "ENGL 103": ClassInfo(rooms={"LAAH": 64}),
            "ENGL 104": ClassInfo(rooms={"LAAH": 34}),
            "ENGR 102": ClassInfo(rooms={"ZACH": 28, "BLOC": 40, "ILCB": 31}),
            "MATH 151": ClassInfo(rooms={"ILCB": 40, "HEB": 20}),
            "ENGR 216": ClassInfo(rooms={"ZACH": 50, "BLOC": 12, "HELD": 28}),
            "PHYS 216": ClassInfo(rooms={"ZACH": 50, "BLOC": 12, "HELD": 28}),
            "MATH 152": ClassInfo(rooms={"ILCB": 50, "HEB": 20 }),
            "PHYS 206": ClassInfo(rooms={"MPHY": 50}),
            "CHEM 120": ClassInfo(rooms={"HELD": 34}),
            "PHYS 207": ClassInfo(rooms={"MPHY": 53}),
            "MATH 251": ClassInfo(rooms={"HELD": 52}),
            "STAT 211": ClassInfo(rooms={"HECC": 23}),
            "ECEN 215": ClassInfo(rooms={"ZACH": 50}),
            "ENGR 217": ClassInfo(rooms={"ZACH": 65}),
            "PHYS 217": ClassInfo(rooms={"ZACH": 62}),
            "MEEN 210": ClassInfo(rooms={"ZACH": 73}),
            "MEEN 260": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 223": ClassInfo(rooms={"HECC": 50}),
            "MEEN 225": ClassInfo(rooms={"ZACH": 40, "JCAIN": 28}),
            "MEEN 315": ClassInfo(rooms={"ZACH": 63}),
            "MATH 308": ClassInfo(rooms={"BLOC": 23}),
            "MEEN 305": ClassInfo(rooms={"JCAIN": 82}),
            "MEEN 344": ClassInfo(rooms={"ZACH": 47}),
            "MEEN 345": ClassInfo(rooms={"ZACH": 26}),
            "MEEN 357": ClassInfo(rooms={"ZACH": 92}),
            "MEEN 360": ClassInfo(rooms={"ZACH": 103}),
            "MEEN 361": ClassInfo(rooms={"ZACH": 89}),
            "MEEN 364": ClassInfo(rooms={"JCAIN": 87}),
            "MEEN 365": ClassInfo(rooms={"ZACH": 43}),
            "ISEN 302": ClassInfo(rooms={"ZACH": 96}),
            "MEEN 363": ClassInfo(rooms={"HECC": 40, "JCAIN": 28}),
            "MEEN 368": ClassInfo(rooms={"HECC": 60}),
            "MEEN 381": ClassInfo(rooms={"ARCB": 20}),
            "MEEN 401": ClassInfo(rooms={"JCAIN": 25}),
            "MEEN 461": ClassInfo(rooms={"ZACH": 67}),
            "MEEN 464": ClassInfo(rooms={"ZACH": 88}),
            "MEEN 423": ClassInfo(rooms={"JCAIN": 78}),
            "MEEN 439": ClassInfo(rooms={"ZACH": 21}),
            "MEEN 442": ClassInfo(rooms={"ZACH": 43}),
            "MEEN 402": ClassInfo(rooms={"JCAIN": 56,"ZACH": 29}),
            "MEEN 404": ClassInfo(rooms={"JCAIN": 43, "HECC": 5}),
            # Additional electives that we are FORCED to take :(
        }
    )

    CHEM = DegreePlan(
        name="CHEM",
        classes={
            "CHEM 100": ClassInfo(rooms={"PETE": 35, "CHEM": 13}),
            "CHEM 119": ClassInfo(rooms={"CHEM": 307}),
            "ENGL 104": ClassInfo(rooms={"LAAH": 64}),
            "ENGL 210": ClassInfo(rooms={"LAAH": 30}),
            "MATH 151": ClassInfo(rooms={"HEB": 68, "BLOC": 43}),
            "MATH 171": ClassInfo(rooms={"BLOC": 42, "HEB": 67}),
            "CHEM 120": ClassInfo(rooms={"CHEM": 110, "HELD": 28, "HEB": 73}),
            "MATH 152": ClassInfo(rooms={"BLOC": 40, "HEB": 60}),
            "MATH 172": ClassInfo(rooms={"BLOC": 76, "ILSB": 34}),
            "CHEM 227": ClassInfo(rooms={"ILCB": 210, "CHEM": 23}),
            "CHEM 237": ClassInfo(rooms={"CHEM": 40, "ILSB": 65}),
            "CHEM 228": ClassInfo(rooms={"ILCB": 210, "CHEM": 23}),
            "CHEM 238": ClassInfo(rooms={"CHEM": 205, "ILCB": 82}),
            "CHEM 315": ClassInfo(rooms={"CHEM": 303}),
            "CHEM 318": ClassInfo(rooms={"ILSB": 40, "CHEM": 305}),
            "CHEM 327": ClassInfo(rooms={"CHEM": 202}),
            "CHEM 328": ClassInfo(rooms={"CHEM": 340, "ILSB": 39}),
            "CHEM 362": ClassInfo(rooms={"CHEM": 87}),
            "CHEM 383": ClassInfo(rooms={"CHEM": 303}),
            "CHEM 412": ClassInfo(rooms={"CHEM": 85}),
            "CHEM 413": ClassInfo(rooms={"CHEM": 40}),
            "CHEM 414": ClassInfo(rooms={"CHEM": 304}),
            "CHEM 415": ClassInfo(rooms={"CHEM": 87}),
            "CHEM 446": ClassInfo(rooms={"CHEM": 66}),
            "CHEM 456": ClassInfo(rooms={"CHEM": 134}),
            "CHEM 463": ClassInfo(rooms={"CHEM": 78}),
            "CHEM 464": ClassInfo(rooms={"CHEM": 456}),
            "CHEM 466": ClassInfo(rooms={"CHEM": 353}),
            "CHEM 468": ClassInfo(rooms={"CHEM": 241}),
            "CHEM 481": ClassInfo(rooms={"CHEM": 26}),
            "CHEM 483": ClassInfo(rooms={"CHEM": 74}),
            "CHEM 485": ClassInfo(rooms={"CHEM": 12}),
            "CHEM 491": ClassInfo(rooms={"CHEM": 363}),
            # Additional electives 
        }
    )

    CSCE = DegreePlan(
        name="CSCE",
        classes={
            "CSCE 121": ClassInfo(rooms={"ZACH": 45, "HRBB": 21}),
            "CSCE 181": ClassInfo(rooms={"ZACH": 67, "PETR": 21}),
            "MATH 151": ClassInfo(rooms={"HEB": 68, "BLOC": 45}),
            "MATH 171": ClassInfo(rooms={"HEB": 68, "BLOC": 23}),
            "ENGL 104": ClassInfo(rooms={"LAAH": 45}),
            "PHYS 206": ClassInfo(rooms={"MPHY": 90}),
            "PHYS 226": ClassInfo(rooms={"ILSB": 45, "HELD": 65}),
            "CSCE 221": ClassInfo(rooms={"ZACH": 55}),
            "CSCE 222": ClassInfo(rooms={"ZACH": 59}),
            "CSCE 312": ClassInfo(rooms={"ZACH":65}),
            "CSCE 313": ClassInfo(rooms={"ZACH": 57, "AGLS": 67}),
            "CSCE 314": ClassInfo(rooms={"HEB": 65, "PETR": 76}),
            "CSCE 315": ClassInfo(rooms={"ZACH": 56, "HRBB": 87}),
            "CSCE 411": ClassInfo(rooms={"HRBB": 43, "ZACH": 98}),
            "CSCE 433": ClassInfo(rooms={"ACAD": 67, "ZACH": 78}),
            "CSCE 481": ClassInfo(rooms={"ACAD": 89, "ZACH": 32}),
            "CSCE 482": ClassInfo(rooms={"HRBB": 32, "ACAD": 65, "ZACH": 34}),
            "MATH 304": ClassInfo(rooms={"BLOC": 56, "HEB": 45}),
            "MATH 308": ClassInfo(rooms={"BLOC": 93, "HELD": 45}),
            "STAT 211": ClassInfo(rooms={"HECC": 63, "BLOC": 76}),
        }
    )

    return {"MEEN": MEEN, "CHEM": CHEM, "CSCE": CSCE}
