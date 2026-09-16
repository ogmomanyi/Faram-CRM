import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/products')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => console.error('Error fetching products:', error));
    }, []);

    return (
        <div>
            <h2>Products</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Product</th>
                        <th>Supplier</th>
                        <th>Contact Person</th>
                        <th>Phone</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.ID}>
                            <td>{product.ID}</td>
                            <td>{product.Product}</td>
                            <td>{product.Supplier}</td>
                            <td>{product.Contact_Person}</td>
                            <td>{product.Phone}</td>
                            <td>{product.Email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Products;
