import React from 'react';
import ReactDOM from 'react-dom/client';
import './css/index.css';
import TopBar from './components/TopBar';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
    <div>
      <TopBar />
    </div>
);
