import React, { useState } from 'react';
import '../css/TopBar.css';


interface BtnProps {
    label: string;  
    tabName: string;
    activeTab: string;
    setActiveTab: (tab: string) => void;   
}
function Btn({ label, tabName, activeTab, setActiveTab }: BtnProps) {
    return(
        <button className={activeTab === tabName ? 'tab active' : 'tab'} 
                onClick={() => setActiveTab(tabName)}>
            {label}
        </button>
    );
}

export default Btn;