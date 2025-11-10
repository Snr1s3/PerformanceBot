import React from 'react';
import '../../css/CpuInfoCard.css';
import CpuUsagePie from '../Pie.tsx';
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
  const coreUsageEntries: Array<[string, number]> = Array.isArray(cpu.cpu_core)
    ? cpu.cpu_core.flatMap(o => Object.entries(o))
    : Object.entries(cpu.cpu_core || {});

  const freqEntries: Array<[string, number]> = Array.isArray(cpu.frequency_core)
    ? cpu.frequency_core.flatMap(o => Object.entries(o))
    : cpu.frequency_core
      ? Object.entries(cpu.frequency_core)
      : [];

  return (
    <div className="cpu-card">
      <h3>CPU Information</h3>

      <div className="cpu-summary-grid">
        <div className="cpu-metric-tile">
          <strong>Cores</strong>
          <div className="cpu-metric-value">{cpu.cores_count}</div>
        </div>
        <div className="cpu-metric-tile">
          <strong>Threads</strong>
          <div className="cpu-metric-value">{cpu.threads_count}</div>
        </div>
        <div className="cpu-metric-tile">
          <strong>Total Usage</strong>
            <CpuUsagePie percent={cpu.cpu} />
        </div>
        <div className="cpu-metric-tile">
          <strong>Avg Freq</strong>
          <div className="cpu-metric-value">{cpu.frequency.toFixed(2)} Hz</div>
        </div>
      </div>
      {coreUsageEntries.length > 0 && (
        <>
          <div className="cpu-section-title">Per-Core Usage</div>
          <div className="cpu-cores-grid">
            {coreUsageEntries.map(([core, val]) => (
              <div key={core} className="cpu-core-item">
                <div className="cpu-core-label">{core}</div>
                <CpuUsagePie percent={Number(val.toFixed(2))} />
              </div>
            ))}
          </div>
        </>
      )}

      {freqEntries.length > 0 && (
        <>
          <div className="cpu-section-title">Per-Core Frequency</div>
            <div className="cpu-cores-grid">
              {freqEntries.map(([core, val]) => (
                <div key={core} className="cpu-core-item">
                  <div className="cpu-core-label">{core}</div>
                  <div>{val.toFixed(2)} Hz</div>
                </div>
              ))}
            </div>
        </>
      )}
    </div>
  );
}

export default CpuInfoCard;