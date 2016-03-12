###### Resource
* http://www.thegeekstuff.com/2012/09/sqlite-command-examples/

###### Create a DB and a table
* sqlite3 company.db
* sqlite> create table employee(empid integer,name varchar(20),title varchar(10));
* sqlite> create table department(deptid integer,name varchar(20),location varchar(10));
* sqlite> .quit

###### Insert Records
* insert into employee values(101,'John Smith','CEO');
* insert into department values(1,'Sales','Los Angeles');
* or
* echo "insert into employee values(101,'John Smith','CEO');" > insert-data.sql
* sqlite3 company.db < insert-data.sql

###### View Recods
* sqlite3 company.db
* sqlite> select * from employee;
* sqlite> select * from department;

###### Rename a Table
* sqlite> alter table department rename to dept;

######  Add a Column to an Existing Table
* sqlite> alter table employee add column deptid integer;
* update employee set deptid=3 where empid=101;
* update employee set deptid=2 where empid=102;
* sqlite> select * from employee;

###### View all Tables in a Database
* sqlite> .tables

###### Create an Index
* sqlite> create unique index empidx on employee(empid);
* Once an unique index is created, if you try to add another record with an empid that already exists, you’ll get an error

###### Create a Trigger
* sqlite> alter table employee add column updatedon date;
* vi employee_update_trg.sql
  * create trigger employee_update_trg after update on employee
  * begin
  *   update employee set updatedon = datetime('NOW') where rowid = new.rowid;
  * end;
* sqlite3 company.db < employee_update_trg.sql

###### Create a View
* sqlite> create view empdept as select empid, e.name, title, d.name, location from employee e, dept d where e.deptid = d.deptid;
* sqlite> select * from empdept;
* sqlite> .tables

###### SQLite Savepoint, Rollback, Commit
* sqlite> savepoint major;
* sqlite> insert into dept values(4,'HR','Los Angeles');
* sqlite> rollback to savepoint major;
* If you don’t want your savepoints anymore, you can erase it using release command.
* sqlite> release savepoint major;

###### Additional Date Functions
* sqlite> select empid,datetime(updatedon,'localtime') from employee;
* sqlite> select empid,strftime('%d-%m-%Y %w %W',updatedon) from employee;

###### Dropping Objects
* sqlite> drop index empidx;
* sqlite> drop trigger employee_update_trg;
* sqlite> drop view empdept;
* sqlite> drop table employee;
* sqlite> drop table dept;

