import React from 'react';
import Metric from './Metric.tsx';

interface MemoryInfoCardProps {
    memoryInfo: {
        ram_total: number;
        ram_available: number;
        ram_percent: number;
    };
}

function MemoryInfoCard({ memoryInfo }:MemoryInfoCardProps) {
    return (
        <div className="card">
            <h3>Memory Information</h3>
            <Metric label="Ram Total" value={memoryInfo.ram_total} />
            <Metric label="Ram Available" value={memoryInfo.ram_available} />
            <Metric label="Ram Percent" value={memoryInfo.ram_percent} />
        </div>
    );
}

export default MemoryInfoCard;