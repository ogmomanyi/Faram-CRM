import React from 'react';
import Clients from './components/Clients';
import Leads from './components/Leads';
import Suppliers from './components/Suppliers';
import Products from './components/Products';

function App() {
    return (
        <div className="App">
            <h1>CRM Application</h1>
            <Clients />
            <Leads />
            <Suppliers />
            <Products />
        </div>
    );
}

export default App;
