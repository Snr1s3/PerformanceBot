import React from 'react';
import '../css/TopBar.css';
import Btn from './Button';

function TopBar() {
    return (
        <div className="topbar">
        <h1>Performance Dashboard</h1>
            <Btn label="Dashboard" tabName="dashboard" />
            <Btn label="System" tabName="system" />
        </div>
    );
}


export default TopBar;