

CREATE table Books(
    book_id INT PRIMARY KEY,
    author_id INT ,
    FOREIGN KEY(author_id) REFERENCES Author(author_id),
    price DOUBLE,
    publication_date DATE
);



CREATE TABLE Author(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);



CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);


CREATE TABLE Orders
(
    order_id INT PRIMARY KEY,
    customer_id INT ,
    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
    order_date DATE
);

CREATE TABLE Order_Details(
    orderdetail INT PRIMARY KEY,
    book_id INT ,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    quantity DOUBLE
);









