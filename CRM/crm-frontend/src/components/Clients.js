import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Clients() {
    const [clients, setClients] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/clients')
            .then(response => {
                setClients(response.data);
            })
            .catch(error => console.error('Error fetching clients:', error));
    }, []);

    return (
        <div>
            <h2>Clients</h2>
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
                    {clients.map(client => (
                        <tr key={client.ID}>
                            <td>{client.ID}</td>
                            <td>{client.Name}</td>
                            <td>{client.Contact_Person}</td>
                            <td>{client.Phone}</td>
                            <td>{client.Email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Clients;
