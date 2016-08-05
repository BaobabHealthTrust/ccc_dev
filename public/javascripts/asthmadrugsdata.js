<!--

var generic = [ "SALBUTAMOL",
                "PREDNISOLONE",
                "HYDROCORTISONE",
                "DEXAMETHASONE",
                "MAGNESIUM SULPHATE"];

var drugs = {"HYDROCORTISONE":[
                ["25mg/ml","OD","Hydrocortisone Acetate 25mg/ml","5.0","ml","One per day"],
                ["25mg/ml","BD","Hydrocortisone Acetate 25mg/ml","5.0","ml","Two per day"],
                ["25mg/ml","TDS","Hydrocortisone Acetate 25mg/ml","5.0","ml","Three per day"],
                ["15g","OD","Hydrocortisone Cream 1% (15g Tube)","1.0","application","One per day"],
                ["15g","BD","Hydrocortisone Cream 1% (15g Tube)","1.0","application","Two per day"],
                ["15g","TDS","Hydrocortisone Cream 1% (15g Tube)","1.0","application","Three per day"],
                ["20mg","OD","Hydrocortisone (20mg Tablet)","1.0","tab(s)","One per day"],
                ["20mg","BD","Hydrocortisone (20mg Tablet)","1.0","tab(s)","Two per day"],
                ["20mg","TDS","Hydrocortisone (20mg Tablet)","1.0","tab(s)","Three per day"],
                ["50mg/ml","OD","Hydrocortisone Iv (50mg/ml Injection)","2.0","ml","One per day"],
                ["50mg/ml","BD","Hydrocortisone Iv (50mg/ml Injection)","2.0","ml","Two per day"],
                ["50mg/ml","TDS","Hydrocortisone Iv (50mg/ml Injection)","2.0","ml","Three per day"],
                ["10mg","OD","Hydrocortisone (10mg Tablet)","1.0","tab(s)","One per day"],
                ["10mg","BD","Hydrocortisone (10mg Tablet)","1.0","tab(s)","Two per day"],
                ["10mg","TDS","Hydrocortisone (10mg Tablet)","1.0","tab(s)","Three per day"],
                ["30mg","OD","Hydrocortisone (30mg Tablet)","1.0","tab(s)","One per day"],
                ["30mg","BD","Hydrocortisone (30mg Tablet)","1.0","tab(s)","Two per day"],
                ["30mg","TDS","Hydrocortisone (30mg Tablet)","1.0","tab(s)","Three per day"]
                ],
            "PREDNISOLONE":[
                ["10mg","OD","Prednisolone (10mg)","1.0","tab(s)","One per day"],
                ["10mg","BD","Prednisolone (10mg)","1.0","tab(s)","Two per day"],
                ["10mg","TDS","Prednisolone (10mg)","1.0","tab(s)","Three per day"],
                ["5mg","OD","Prednisolone (5mg Tablet)","1.0","tab(s)","One per day"],
                ["5mg","BD","Prednisolone (5mg Tablet)","1.0","tab(s)","Two per day"],
                ["5mg","TDS","Prednisolone (5mg Tablet)","1.0","tab(s)","Three per day"],
                ["40mg","OD","Prednisolone (40mg)","1.0","tab(s)","One per day"],
                ["40mg","BD","Prednisolone (40mg)","1.0","tab(s)","Two per day"],
                ["40mg","TDS","Prednisolone (40mg)","1.0","tab(s)","Three per day"],
                ["60mg","OD","Prednisolone (60mg)","1.0","tab(s)","One per day"],
                ["60mg","BD","Prednisolone (60mg)","1.0","tab(s)","Two per day"],
                ["60mg","TDS","Prednisolone (60mg)","1.0","tab(s)","Three per day"],
                ["20mg","OD","Prednisolone (20 Mg)","1.0","tab(s)","One per day"],
                ["20mg","BD","Prednisolone (20 Mg)","1.0","tab(s)","Two per day"],
                ["20mg","TDS","Prednisolone (20 Mg)","1.0","tab(s)","Three per day"],
                ["15mg","OD","Prednisolone (15mg)","1.0","tab(s)","One per day"],
                ["15mg","BD","Prednisolone (15mg)","1.0","tab(s)","Two per day"],
                ["15mg","TDS","Prednisolone (15mg)","1.0","tab(s)","Three per day"],
                ["30mg","OD","Prednisolone (30 Mg)","1.0","tab(s)","One per day"],
                ["30mg","BD","Prednisolone (30 Mg)","1.0","tab(s)","Two per day"],
                ["30mg","TDS","Prednisolone (30 Mg)","1.0","tab(s)","Three per day"]
                ],
            "MAGNESIUM SULPHATE":[
                ["50%","OD","Magnesium Sulphate (50%)","2.0","ml","One per day"],
                ["50%","BD","Magnesium Sulphate (50%)","2.0","ml","Two per day"],
                ["50%","TDS","Magnesium Sulphate (50%)","2.0","ml","Three per day"]
                ],
            "SALBUTAMOL":[
                ["4mg","OD","Salbutamol (4mg Tablet)","1.0","tab(s)","One per day"],
                ["4mg","BD","Salbutamol (4mg Tablet)","1.0","tab(s)","Two per day"],
                ["4mg","TDS","Salbutamol (4mg Tablet)","1.0","tab(s)","Three per day"],
                ["100mcg","OD","Salbutamol Mdi (100mcg/Dose)","100.0","mcg","One per day"],
                ["100mcg","BD","Salbutamol Mdi (100mcg/Dose)","100.0","mcg","Two per day"],
                ["100mcg","TDS","Salbutamol Mdi (100mcg/Dose)","100.0","mcg","Three per day"],
                ["5mg/ml","OD","Salbutamol (Resp Solution 5mg/ml)","30.0","ml","One per day"],
                ["5mg/ml","BD","Salbutamol (Resp Solution 5mg/ml)","30.0","ml","Two per day"],
                ["5mg/ml","TDS","Salbutamol (Resp Solution 5mg/ml)","30.0","ml","Three per day"],
                ["1mg/ml","OD","Salbutamol Sulphate 1mg/ml","5.0","ml","One per day"],
                ["1mg/ml","BD","Salbutamol Sulphate 1mg/ml","5.0","ml","Two per day"],
                ["1mg/ml","TDS","Salbutamol Sulphate 1mg/ml","5.0","ml","Three per day"]
                ],
            "DEXAMETHASONE":[
                ["05mg","OD","Dexamethasone (0.5mg Tablet)","1.0","tab(s)","One per day"],
                ["05mg","BD","Dexamethasone (0.5mg Tablet)","1.0","tab(s)","Two per day"],
                ["05mg","TDS","Dexamethasone (0.5mg Tablet)","1.0","tab(s)","Three per day"],
                ["5mg/ml","OD","Dexamethasone (5mg/ml Injection)","5.0","ml","One per day"],
                ["5mg/ml","BD","Dexamethasone (5mg/ml Injection)","5.0","ml","Two per day"],
                ["5mg/ml","TDS","Dexamethasone (5mg/ml Injection)","5.0","ml","Three per day"],
                ["1mg","OD","Dexamethasone Injection (1 Mg)","1.0","tab(s)","One per day"],
                ["1mg","BD","Dexamethasone Injection (1 Mg)","1.0","tab(s)","Two per day"],
                ["1mg","TDS","Dexamethasone Injection (1 Mg)","1.0","tab(s)","Three per day"],
                ["2mg","OD","Dexamethasone Injection (2 Mg)","1.0","tab(s)","One per day"],
                ["2mg","BD","Dexamethasone Injection (2 Mg)","1.0","tab(s)","Two per day"],
                ["2mg","TDS","Dexamethasone Injection (2 Mg)","1.0","tab(s)","Three per day"],
                ["4mg","OD","Dexamethasone Injection (4 Mg)","1.0","tab(s)","One per day"],
                ["4mg","BD","Dexamethasone Injection (4 Mg)","1.0","tab(s)","Two per day"],
                ["4mg","TDS","Dexamethasone Injection (4 Mg)","1.0","tab(s)","Three per day"],
                ["5mg","OD","Dexamethasone Injection (5 Mg)","1.0","tab(s)","One per day"],
                ["5mg","BD","Dexamethasone Injection (5 Mg)","1.0","tab(s)","Two per day"],
                ["5mg","TDS","Dexamethasone Injection (5 Mg)","1.0","tab(s)","Three per day"],
                ["10mg","OD","Dexamethasone Injection (10 Mg)","1.0","tab(s)","One per day"],
                ["10mg","BD","Dexamethasone Injection (10 Mg)","1.0","tab(s)","Two per day"],
                ["10mg","TDS","Dexamethasone Injection (10 Mg)","1.0","tab(s)","Three per day"]
                ]};


//-->