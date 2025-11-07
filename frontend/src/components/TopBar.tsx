import React, { useEffect, useState } from 'react';
import '../css/TopBar.css';
import Btn from './Button';  // Remove 'components/'
import SystemInfoCard from './cards/SystemInfoCard';  // Remove 'components/'
import CpuInfoCard from './cards/CpuInfoCard';  // Remove 'components/'


interface SystemData {
    timestamp: string;
    system_info: {
        platform: string;
        node: string;
        release: string;
        version: string;
        machine: string;
    };
    cpu: {
        cpu: number;
        cores_count: number;
        threads_count: number;
        frequency: number;
        cpu_core: { [key: string]: number };
    };
}


function TopBar() {
    const [activeTab, setActiveTab] = useState('dashboard');
    const [data, setData] = useState<SystemData | null>(null);
    useEffect(() => {
        const ws = new WebSocket('ws://127.0.0.1:8000/ws');
        
        ws.onopen = () => {
        console.log('Connected to WebSocket');
        };
        
        ws.onmessage = (event) => {
        const jsonData = JSON.parse(event.data);
        console.log('Received data:', jsonData);
        setData(jsonData);  
        };
        
        ws.onclose = () => {
        console.log('WebSocket closed');
        };
        
        
        return () => {
        ws.close();
        };
    }, []);  
    return (
        <div>
            <div className="topbar">
                <h1>Performance Dashboard</h1>
                <div className='tabs'>
                    <Btn label="Dashboard" tabName="dashboard" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="System Info" tabName="system" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="CPU" tabName="cpu" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Memory" tabName="memory" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Network" tabName="network" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Sensor" tabName="sensor" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Other" tabName="other" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Docker" tabName="docker" activeTab={activeTab} setActiveTab={setActiveTab} />
                </div>
            </div>
            {activeTab === 'dashboard' && (<pre>{JSON.stringify(data, null, 2)}</pre>)}
            {activeTab === 'system' && data?.system_info && (
                <SystemInfoCard systemInfo={data.system_info} />
            )}
        </div>
    );
}


export default TopBar;