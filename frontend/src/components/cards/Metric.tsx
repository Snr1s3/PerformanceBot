import React from 'react';

interface MetricProps {
    label: string;
    value: string | number;
    suffix?: string;  // Optional with ?
}

function Metric({ label, value, suffix }: MetricProps) {
    return (
        <div className="metric">
            <span className="metric-label">{label}: </span>
            <span className="metric-value">
                {value}{suffix && suffix}
            </span>
        </div>
    );
}

export default Metric;