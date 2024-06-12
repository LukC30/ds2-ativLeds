create database db_led;

use db_led;

create table tbl_led(
id int unsigned auto_increment primary key,
nome varchar(20),
criado_em timestamp default now()

 
);

select * from tbl_led;