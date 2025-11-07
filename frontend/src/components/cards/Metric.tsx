import React from 'react';

interface MetricProps {
    label: string;
    value: string | number;
    prefix?: string;  // Optional with ?
}

function Metric({ label, value, prefix }: MetricProps) {
    return (
        <div className="metric">
            <span className="metric-label">{label}: </span>
            <span className="metric-value">
                {value}{prefix && prefix}
            </span>
        </div>
    );
}

export default Metric;