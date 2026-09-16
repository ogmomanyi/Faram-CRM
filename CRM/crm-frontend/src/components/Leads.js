import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Leads() {
    const [leads, setLeads] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/leads')
            .then(response => {
                setLeads(response.data);
            })
            .catch(error => console.error('Error fetching leads:', error));
    }, []);

    return (
        <div>
            <h2>Leads</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Date Created</th>
                        <th>Lead Status</th>
                        <th>Client Name</th>
                        <th>Product</th>
                        <th>Value</th>
                        <th>Supplier Name</th>
                        <th>Lead Owner</th>
                        <th>Lead Source</th>
                        <th>Notes</th>
                    </tr>
                </thead>
                <tbody>
                    {leads.map(lead => (
                        <tr key={lead.ID}>
                            <td>{lead.ID}</td>
                            <td>{lead.Date_Created}</td>
                            <td>{lead.Lead_Status}</td>
                            <td>{lead.Client_Name}</td>
                            <td>{lead.Product}</td>
                            <td>{lead.Value}</td>
                            <td>{lead.Supplier_Name}</td>
                            <td>{lead.Lead_Owner}</td>
                            <td>{lead.Lead_Source}</td>
                            <td>{lead.Notes}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Leads;
