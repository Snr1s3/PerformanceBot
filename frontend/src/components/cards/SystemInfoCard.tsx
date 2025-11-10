import React from 'react';
import Metric from './Metric.tsx';
import '../../css/SystemInfoCard.css';


interface UserInfo {
    name: string;
    terminal: string;
    host: string;
    started: number;
    pid: number;
}
interface SystemInfoCardProps {
    system_info: {
        platform: string;
        node: string;
        release: string;
        version: string;
        machine: string;
        boottime: string;
        uptime_seconds: number;
        users_count: number;
        users?: UserInfo[];
    };
}

function formatUptime(sec: number) {
    if (!sec || sec < 0) return 'n/a';
    const d = Math.floor(sec / 86400);
    const h = Math.floor((sec % 86400) / 3600);
    const m = Math.floor((sec % 3600) / 60);
    const s = sec % 60;
    return [
        d ? `${d}d` : '',
        (h || d) ? `${h}h` : '',
        (m || h || d) ? `${m}m` : '',
        `${s}s`
    ].filter(Boolean).join(' ');
}

function formatStarted(epochSec: number) {
    const d = new Date(epochSec * 1000);
    return d.toISOString().replace('T', ' ').slice(0, 19);
}

function SystemInfoCard({ system_info }: SystemInfoCardProps) {
    const uptimeStr = formatUptime(system_info.uptime_seconds);
    const bootDisplay = system_info.boottime.replace('T', ' ');
    const users = system_info.users ?? [];
    return (
        <div className="card system-card">
        <h3 className="card-title">System Information</h3>
        <div className="metrics-grid">
            <Metric label="Platform" value={system_info.platform} />
            <Metric label="Hostname" value={system_info.node} />
            <Metric label="Kernel" value={system_info.release} />
            <Metric label="Architecture" value={system_info.machine} />
            <Metric label="Version" value={system_info.version} />
            <Metric label="Boot Time" value={bootDisplay} />
            <Metric label="Uptime" value={uptimeStr} />
            <Metric label="Users" value={system_info.users_count} />
        </div>

        <div style={{ marginTop: 26 }}>
            <h4 style={{ margin: '0 0 10px', fontWeight: 600 }}>Logged-in Users</h4>
            <div
                style={{
                    display: 'grid',
                    gap: 8,
                    gridTemplateColumns: 'repeat(auto-fill,minmax(260px,1fr))'
                }}
                >
                {users.map(u => (
                    <div
                    key={`${u.name}-${u.pid}`}
                    style={{
                        background: 'var(--bg-tile)',
                        border: '1px solid var(--border-color)',
                        borderRadius: 8,
                        padding: '8px 10px',
                        fontSize: '.72rem',
                        lineHeight: 1.25
                    }}
                    >
                    <div>
                        <strong>User:</strong> {u.name}
                    </div>
                    <div>
                        <strong>TTY:</strong> {u.terminal}
                    </div>
                    <div>
                        <strong>Host:</strong> {u.host}
                    </div>
                    <div>
                        <strong>Started:</strong> {formatStarted(u.started)}
                    </div>
                    <div>
                        <strong>PID:</strong> {users.length === 0 ? 0 : u.pid}
                    </div>
                    </div>
                ))}
                </div>
            </div>
        </div>
    );
}

export default SystemInfoCard;