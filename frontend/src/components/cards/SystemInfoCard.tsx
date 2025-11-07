import React from 'react';
import Metric from './Metric.tsx';

interface SystemInfoCardProps {
    system_info: {
        platform: string;
        node: string;
        release: string;
        version: string;
        machine: string;
        boottime:string;
        uptime_seconds:number;
        users_count: number;
    };
}

function SystemInfoCard({ system_info }: SystemInfoCardProps) {
    const totalSec = system_info.uptime_seconds;
    const days = Math.floor(totalSec / 86400);
    const hours = Math.floor((totalSec % 86400) / 3600);
    const minutes = Math.floor((totalSec % 3600) / 60);
    const seconds = totalSec % 60;

    const uptimeStr = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    return (
        <div className="card">
            <h3>System Information</h3>
            <Metric label="Platform" value={system_info.platform} />
            <Metric label="Node" value={system_info.node} />
            <Metric label="Release" value={system_info.release} />
            <Metric label="Machine" value={system_info.machine} />
            <Metric label="Boottime" value={system_info.boottime} />
            <Metric label="Uptime" value={uptimeStr}/>
            <Metric label="User Count" value={system_info.users_count} />
        </div>
    );
}

export default SystemInfoCard;