import { useEffect, useState } from 'react';
import '../css/TopBar.css';
import Btn from './Button.tsx';
import SystemInfoCard from './cards/SystemInfoCard.tsx'; 
import CpuInfoCard from './cards/CpuInfoCard.tsx';  
import MemoryInfoCard from './cards/MemoryInfoCard.tsx';

interface UserInfo {
    name: string;
    terminal: string;
    host: string;
    started: number;
    pid: number;
}

interface SystemData {
    system_info: {
        platform: string;
        node: string;
        release: string;
        version: string;
        machine: string;
        boottime:string;
        uptime_seconds:number;
        users_count: number;
        users?:UserInfo[];
    };
    cpu: {
        cpu: number;
        cores_count: number;
        threads_count: number;
        frequency: number;
        cpu_core: { [key: string]: number };
    };

    memory: {
        ram_total: number;
        ram_available: number;
        ram_percent: number;
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
        <div className="app">
            <div className="topbar">
                <h1>Performance Dashboard</h1>
                <div className='tabs'>
                    <Btn label="Dashboard" tabName="dashboard" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="System Info" tabName="system" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="CPU" tabName="cpu" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Memory" tabName="memory" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Network" tabName="network" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Sensor" tabName="sensor" activeTab={activeTab} setActiveTab={setActiveTab} />
                    <Btn label="Docker" tabName="docker" activeTab={activeTab} setActiveTab={setActiveTab} />
                </div>
            </div>
            <div className="content-area">
                {activeTab === 'dashboard' && (
                    <pre style={{margin:0, background:'#141418', color:'#eee', padding:'12px', borderRadius:8, overflow:'auto'}}>
                      {data ? JSON.stringify(data, null, 2) : 'Waiting for data...'}
                    </pre>
                )}
                {activeTab === 'system' && data?.system_info && (
                    <SystemInfoCard system_info={data.system_info} />
                )}
                {activeTab === 'cpu' && data?.cpu && (
                    <CpuInfoCard cpu={data.cpu} />
                )}
                {activeTab === 'memory' && data?.memory && (
                    <MemoryInfoCard memoryInfo={data.memory} />
                )}
            </div>
        </div>
    );
}


export default TopBar;