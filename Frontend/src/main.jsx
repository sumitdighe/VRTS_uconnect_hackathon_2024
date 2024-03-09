import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import SmoothScrollWrapper from './smoother';

ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>
    <SmoothScrollWrapper>
    <App />
        </SmoothScrollWrapper>
  //</React.StrictMode>,
)
