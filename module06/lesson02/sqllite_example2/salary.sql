-- Table: companies
DROP TABLE IF EXISTS companies;
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: employees
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee VARCHAR(255) UNIQUE NOT NULL,
    post VARCHAR(120) NOT NULL,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: payments
DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    date_of DATE NOT NULL,
    total INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);