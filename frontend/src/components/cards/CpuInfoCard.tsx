import React from 'react';
import Metric from './Metric';

interface CpuInfoCardProps {
    cpu: {
        cores_count: number;
        threads_count: number;
        cpu: number;
        frequency: number;
        cpu_core: { [key: string]: number };
    };
}

function CpuInfoCard({ cpu }: CpuInfoCardProps) {
    console.log('CPU data:', cpu);
    console.log('CPU core data:', cpu.cpu_core);
    return (
        <div className="card">
            <h3>CPU Information</h3>
            <Metric label="Cores" value={cpu.cores_count} />
            <Metric label="Threads" value={cpu.threads_count} />
            <Metric label="Usage" value={cpu.cpu} prefix='%' />
            <Metric label="Frequency" value={cpu.frequency} prefix='Hz' />
            <h4>Threads Usage</h4>
            {cpu.cpu_core && Object.entries(cpu.cpu_core).map(([coreName, usage]) => (
                <Metric 
                    key={coreName} 
                    label={coreName} 
                    value={usage} 
                    prefix='%' 
                />
            ))}
        </div>
    );
}

export default CpuInfoCard;