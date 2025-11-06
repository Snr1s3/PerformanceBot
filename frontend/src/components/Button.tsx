import React, { useState } from 'react';
import '../css/TopBar.css';


interface BtnProps {
    label: string;  
    tabName: string;  
}
function Btn({ label, tabName }: BtnProps) {
    const [activeTab, setActiveTab] = useState('dashboard');
    return(
        <button className={activeTab === tabName ? 'tab active' : 'tab'} 
                onClick={() => setActiveTab(tabName)}>
            {label}
        </button>
    );
}

export default Btn;