import React from 'react';
import Metric from './Metric.tsx';

interface CpuInfoCardProps {
  cpu: {
    cores_count: number;
    threads_count: number;
    cpu: number;
    frequency: number;
    cpu_core: Array<Record<string, number>> | { [key: string]: number };
    frequency_core?: Array<Record<string, number>> | { [key: string]: number };
  };
}

function CpuInfoCard({ cpu }: CpuInfoCardProps) {
  // Normalize cpu_core
  const coreUsageEntries: Array<[string, number]> = Array.isArray(cpu.cpu_core)
    ? cpu.cpu_core.flatMap(obj => Object.entries(obj))
    : Object.entries(cpu.cpu_core || {});

  const freqEntries: Array<[string, number]> = Array.isArray(cpu.frequency_core)
    ? cpu.frequency_core.flatMap(obj => Object.entries(obj))
    : cpu.frequency_core
      ? Object.entries(cpu.frequency_core)
      : [];

  return (
    <div className="card">
      <h3>CPU Information</h3>
      <Metric label="Cores" value={cpu.cores_count} />
      <Metric label="Threads" value={cpu.threads_count} />
      <Metric label="Total Usage" value={cpu.cpu} suffix="%" />
      <Metric label="Avg Freq" value={cpu.frequency.toFixed(2)} suffix="Hz" />
      <h4>Per-Core Usage</h4>
      {coreUsageEntries.map(([core, val]) => (
        <Metric key={core} label={core} value={val} suffix="%" />
      ))}
      {freqEntries.length > 0 && (
        <>
          <h4>Per-Core Frequency</h4>
          {freqEntries.map(([core, val]) => (
            <Metric key={core} label={core} value={val.toFixed(2)} suffix="Hz" />
          ))}
        </>
      )}
    </div>
  );
}

export default CpuInfoCard;