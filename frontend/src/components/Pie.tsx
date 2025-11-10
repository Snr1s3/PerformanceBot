import React from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts';

interface Props {
  percent: number; // 0-100
}

const COLORS = ['#0066ff', '#24242a'];

const CpuUsagePie: React.FC<Props> = ({ percent }) => {
  const data = [
    { name: 'Used', value: Number(percent) },
    { name: 'Idle', value: Math.max(0, 100 - Number(percent)) }
  ];
  return (
    <div style={{ width: '100%', height: 240 }}>
      <ResponsiveContainer>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            innerRadius="55%"
            outerRadius="80%"
            startAngle={90}
            endAngle={-270}
            paddingAngle={2}
          >
            {data.map((entry, i) => (
              <Cell key={entry.name} fill={COLORS[i]} stroke="#1f1f24" />
            ))}
          </Pie>
          <Tooltip
            contentStyle={{ background: '#1f1f24', border: '1px solid #2b2b31', fontSize: '.75rem' }}
            formatter={(v: any, n: any) => [`${v.toFixed(2)}%`, n]}
          />
        </PieChart>
      </ResponsiveContainer>
      <div style={{
        position: 'relative',
        marginTop: -150,
        textAlign: 'center',
        fontSize: '1.1rem',
        fontWeight: 600,
        color: '#eee'
      }}>
        {percent.toFixed(1)}%
      </div>
    </div>
  );
};

export default CpuUsagePie;