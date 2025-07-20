CREATE DATABASE salaray_manage_sys ;

CREATE TABLE appuser(
    UserCode int(3) PRIMARY KEY,
    Username char(15),
    Password varchar(10),
    UserType char(5) DEFAULT("admin")
);

CREATE TABLE profession(
    ProfessionCode int(2) PRIMARY KEY,
    ProfessionName varchar(25),
    DailyRate float(11,2)
);

CREATE TABLE employee(
    EmpCode char(5) PRIMARY KEY,
    EmpName varchar(25),
    ProfessionCode int(2),
    FOREIGN KEY (ProfessionCode) REFERENCES profession(ProfessionCode)
);

CREATE TABLE workeddata(
    EmpCode char(5),
    Month int(2),
    Days int(2),
    FOREIGN KEY (EmpCode) REFERENCES employee(EmpCode)
);
