CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATEIME NOT NULL,
    time_out DATEIME NOT NULL,
    cost FLOAT NOT NULL,
    take_away INT NOT NULL,
    staff INT NOT NULL,

    PRIMARY KEY (order_id),
    FOREGN KEY (staff) REFERENCES STAFF (staff_id)
);

CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,

    PRIMARY KEY (product_id)
);

CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,

    PRIMARY KEY (staff_id)
);

CREATE TABLE PRODUCTS_ORDERS (
    product_order_id INT AUTO_INCREMENT NOT NULL,
    product INT NOT NULL,
    in_order INT NOT NULL,
    amount INT NOT NULL,

    PRIMARY KEY (product_order_id)
    FOREGN KEY (product) REFERENCES PRODUCTS (product_id)
    FOREGN KEY (in_order) REFERENCES ORDERS (order_id)
);
