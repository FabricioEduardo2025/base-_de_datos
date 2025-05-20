CREATE DATABASE dominos;
USE dominos;

CREATE TABLE productos (
id_productos INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
tamaño VARCHAR(50) NOT NULL,
precio DECIMAL(10,2) NOT NULL,
codigo_barra VARCHAR(50) PRIMARY KEY
);

CREATE TABLE empleados (
id_empleados INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
apellido VARCHAR(100) ,
telefono VARCHAR(15),
email VARCHAR(100),
direccion TEXT
);

CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
apellido VARCHAR(100),
telefono VARCHAR(15), 
email VARCHAR(100),
direccion TEXT
);

CREATE TABLE proveedores (
id_provedor INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
contacto VARCHAR(100),
telefono VARCHAR(15),
email VARCHAR(100),
direccion TEXT,
tipo ENUM( 'ingredientes' , 'bebidas',
'empaques', 'otros') NOT NULL); 

CREATE TABLE ingredientes (
id_ingrediente INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50),
stock DECIMAL(10,2),
unidad VARCHAR (20)
);

INSERT INTO productos (nombre, tamaño, precio, codigo_barra) VALUES
('Pepperoni', 'Chica', 99.00, '7501000000010'),
('Pepperoni', 'Mediana', 129.00, '7501000000027'),
('Pepperoni', 'Grande', 159.00, '7501000000034'),
('Hawaiana', 'Chica', 105.00, '7501000000041'),
('Hawaiana', 'Mediana', 135.00, '7501000000058'),
('Hawaiana', 'Grande', 165.00, '7501000000065'),
('Mexicana', 'Chica', 110.00, '7501000000072'),
('Mexicana', 'Mediana', 140.00, '7501000000089'),
('Mexicana', 'Grande', 170.00, '7501000000096'),
('Cuatro Quesos', 'Chica', 115.00, '7501000000102'),
('Cuatro Quesos', 'Mediana', 145.00, '7501000000119'),
('Cuatro Quesos', 'Grande', 175.00, '7501000000126');



INSERT INTO empleados (nombre, apellido, telefono, email, direccion) VALUES
('Ana', 'Gómez', '9617654321', 'ana.gomez@dominos.com', 'Av. Las Palmas #45, Tuxtla Gutiérrez'),
('Carlos', 'López', '9611122334', 'carlos.lopez@dominos.com', 'Col. Centro, Tuxtla Gutiérrez'),
('María', 'Ramírez', '9619988776', 'maria.ramirez@dominos.com', 'Zona Norte, Tuxtla Gutiérrez'),
('Luis', 'Martínez', '9613344556', 'luis.martinez@dominos.com', 'Calle Roble #67, Tuxtla Gutiérrez');


INSERT INTO proveedores (nombre, contacto, telefono, email, direccion, tipo)
VALUES ('Bebidas Chiapas', 'Marta López', '9617654321', 'ventas@bebidaschi.mx', 'Blvd. Belisario Domínguez 456, Tuxtla', 'bebidas');

INSERT INTO proveedores (nombre, contacto, telefono, email, direccion, tipo)
VALUES ('Empaques del Sur', 'Carlos Ruiz', '9621122334', 'cruiz@empaques.mx', 'Calle Segunda Norte 22, Tapachula', 'empaques');

INSERT INTO proveedores (nombre, contacto, telefono, email, direccion, tipo)
VALUES ('Varios Express', 'Ana Gómez', '9619988776', 'ana@variosexpress.mx', 'Zona Industrial, Tuxtla Gutiérrez', 'otros');


INSERT INTO clientes (nombre, apellido, telefono, email, direccion) VALUES
('Juan', 'Pérez', '5551234567', 'juan@example.com', 'Calle Falsa 123'),
('María', 'Gómez', '5557654321', 'maria@example.com', 'Av. Reforma 456'),
('Carlos', 'Ramírez', '5559876543', 'carlos@example.com', 'Blvd. Centro 789'),
('Ana', 'López', '5551112222', 'ana@example.com', 'Colonia Juárez 101'),
('Luis', 'Hernández', '5553334444', 'luis@example.com', 'Calle 5 de Mayo 456');


INSERT INTO ingredientes ( nombre, stock, unidad) VALUES
('Queso mozzarella', 25.50, 'kg'),
('Jamón', 10.00, 'kg'),
('Salsa de tomate', 15.75, 'litros'),
('Harina', 50.00, 'kg'),
('Aceitunas', 5.30, 'kg'),
('Pepperoni', 12.25, 'kg'),
('Masa para pizza', 100.00, 'unidades');
