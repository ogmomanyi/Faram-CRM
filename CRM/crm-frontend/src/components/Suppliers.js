import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Suppliers() {
    const [suppliers, setSuppliers] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/suppliers')
            .then(response => {
                setSuppliers(response.data);
            })
            .catch(error => console.error('Error fetching suppliers:', error));
    }, []);

    return (
        <div>
            <h2>Suppliers</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Contact Person</th>
                        <th>Phone</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {suppliers.map(supplier => (
                        <tr key={supplier.ID}>
                            <td>{supplier.ID}</td>
                            <td>{supplier.Name}</td>
                            <td>{supplier.Contact_Person}</td>
                            <td>{supplier.Phone}</td>
                            <td>{supplier.Email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Suppliers;
