import React from 'react';
import Metric from './Metric';

interface SystemInfoCardProps {
    systemInfo: {
        platform: string;
        node: string;
        release: string;
        version: string;
        machine: string;
    };
}

function SystemInfoCard({ systemInfo }: SystemInfoCardProps) {
    return (
        <div className="card">
            <h3>System Information</h3>
            <Metric label="Platform" value={systemInfo.platform} />
            <Metric label="Node" value={systemInfo.node} />
            <Metric label="Release" value={systemInfo.release} />
            <Metric label="Machine" value={systemInfo.machine} />
        </div>
    );
}

export default SystemInfoCard;