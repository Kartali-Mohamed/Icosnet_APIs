# Icosnet API Documentation

## Overview

Welcome to the Icosnet API documentation. This API allows you to manage orders, including reading, creating, searching, updating, and canceling orders. Below, you'll find details on endpoints, request and response formats, as well as any authentication requirements.

## Base URL

All endpoints in this API are relative to the base URL:

```plaintext
http://127.0.0.1:8000/api/
```


### Orders

#### Read Orders

- **Endpoint**: `GET order/`
- **Description**: Retrieve information about all orders.
- **Request**: 
      - ***Method***: `GET`
      - ***URL***: `http://127.0.0.1:8000/api/order/`
- **Response**: 
```json
{
    "detail": "Success",
    "data": [
        {
            "id": "b9434dd4-a5ac-43f5-bb70-8d31107e1530",
            "title": "Second Order",
            "description": "this is the first order",
            "price": "100.00",
            "status": "Shipped",
            "createAt": "2023-11-15T20:40:06.032134Z",
            "user": 1
        },
        {
            "id": "99b5327b-4246-4b0a-b807-c4b8d557ed59",
            "title": "First Order",
            "description": "this is the first order",
            "price": "200.00",
            "status": "Pending",
            "createAt": "2023-11-15T20:54:11.964128Z",
            "user": 1
        }
    ]
}
```

#### Read Order by Id

- **Endpoint**: `GET order/{id}/`
- **Description**: Retrieve an order placed by it Id.
- **Request**: 
      - ***Method***: `GET`
      - ***URL***: `http://127.0.0.1:8000/api/order/{id}/`
- **Response**: 
```json
{
    "detail": "Success",
    "data": {
        "id": "99b5327b-4246-4b0a-b807-c4b8d557ed59",
        "title": "First Order",
        "description": "this is the first order",
        "price": "200.00",
        "status": "Pending",
        "createAt": "2023-11-15T20:54:11.964128Z",
        "user": 1
    }
}
```


#### Create

- **Endpoint**: `POST /order/create/`
- **Description**: Create a new order.
- **Request**: 
      - ***Method***: `POST`
      - ***URL***: `http://127.0.0.1:8000/api/order/create/`
      - ***Body***: 
```json
{
    "title": "First Order",
    "description": "this is the first order",
    "price": "200.00"
}
```
- **Response**: 
```json
{
    "detail": "Order create success"
}
```

#### Update

- **Endpoint**: `PUT /order/update/{id}/`
- **Description**: Update an order.
- **Request**: 
      - ***Method***: `PUT`
      - ***URL***: `http://127.0.0.1:8000/api/update/{id}/`
      - ***Body***: 
```json
{
    "title": "First Order",
    "description": "this is the first order",
    "price": "200.00"
    "status": "Processing"
}
```
- **Response**: 
```json
{
    "detail": "Success",
    "data": {
        "id": "99b5327b-4246-4b0a-b807-c4b8d557ed59",
        "title": "First Order",
        "description": "this is the first order",
        "price": "200.00",
        "status": "Shipped",
        "createAt": "2023-11-15T20:54:11.964128Z",
        "user": 1
    }
}
```

#### Cancel

- **Endpoint**: `DELETE /order/cancel/{id}/`
- **Description**: Cancel an order.
- **Request**: 
      - ***Method***: `DELETE`
      - ***URL***: `http://127.0.0.1:8000/api/order/cancel/{id}/`
- **Response**: 
```json
{
    "detail": "Cancel order is done"
}
```


#### Search

- **Endpoint**: `GET /search/order/`
- **Description**: Search for orders based on title and page.
- **Request**: 
      - *Method*: `GET`
      - *URL*: `http://127.0.0.1:8000/api/search/order/?page=1`
      - *Query Parameters*:
           - `title` (disabled): "First Order"
           - `page`: 1
- **Response**: 
```json
{
    "detail": "Success",
    "data": {
        "id": "99b5327b-4246-4b0a-b807-c4b8d557ed59",
        "title": "First Order",
        "description": "this is the first order",
        "price": "200.00",
        "status": "Shipped",
        "createAt": "2023-11-15T20:54:11.964128Z",
        "user": 1
    }
}
```
