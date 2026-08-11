import React from 'react';
import { Shield, Activity, Lock, AlertTriangle, Terminal } from 'lucide-react';

export default function Home() {
  return (
    <main className="p-8 max-w-7xl mx-auto space-y-8">
      <header className="flex justify-between items-center border-b border-gray-800 pb-4">
        <div className="flex items-center space-x-3">
          <Shield className="w-8 h-8 text-primary" />
          <h1 className="text-2xl font-bold tracking-wider">LLMGuard-X Enterprise</h1>
        </div>
        <div className="flex items-center space-x-2 text-success">
          <div className="w-3 h-3 rounded-full bg-success animate-pulse"></div>
          <span className="font-mono text-sm">SYSTEM SECURE</span>
        </div>
      </header>

      <section className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-gray-900/50 p-6 rounded-lg border border-gray-800">
          <h3 className="text-gray-400 font-mono text-sm mb-2">EVENTS</h3>
          <p className="text-3xl font-bold text-white">1,284</p>
        </div>
        <div className="bg-gray-900/50 p-6 rounded-lg border border-gray-800">
          <h3 className="text-gray-400 font-mono text-sm mb-2">THREATS</h3>
          <p className="text-3xl font-bold text-warning">74</p>
        </div>
        <div className="bg-gray-900/50 p-6 rounded-lg border border-gray-800">
          <h3 className="text-gray-400 font-mono text-sm mb-2">BLOCKED</h3>
          <p className="text-3xl font-bold text-danger">41</p>
        </div>
        <div className="bg-gray-900/50 p-6 rounded-lg border border-gray-800">
          <h3 className="text-gray-400 font-mono text-sm mb-2">RISK LEVEL</h3>
          <p className="text-3xl font-bold text-primary">18%</p>
        </div>
      </section>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <section className="col-span-2 space-y-6">
          <div className="bg-gray-900/30 p-6 rounded-lg border border-gray-800 h-96 flex flex-col justify-center items-center relative overflow-hidden">
             <h2 className="absolute top-4 left-4 font-mono text-sm text-gray-400 flex items-center"><Activity className="w-4 h-4 mr-2"/> REAL-TIME SECURITY PIPELINE</h2>
             <div className="flex space-x-4 text-sm font-mono items-center">
                <span className="text-gray-300">USER</span>
                <span className="text-gray-600">→</span>
                <span className="text-primary border border-primary px-3 py-1 rounded bg-primary/10">RUST GW</span>
                <span className="text-gray-600">→</span>
                <span className="text-purple-400 border border-purple-400 px-3 py-1 rounded bg-purple-400/10">AI ENGINE</span>
                <span className="text-gray-600">→</span>
                <span className="text-success border border-success px-3 py-1 rounded bg-success/10">RISK ENGINE</span>
             </div>
          </div>
        </section>

        <aside className="space-y-6">
          <div className="bg-gray-900/30 p-6 rounded-lg border border-gray-800 h-96">
            <h2 className="font-mono text-sm text-gray-400 mb-4 flex items-center"><Lock className="w-4 h-4 mr-2"/> AI MODEL STATUS</h2>
            <ul className="space-y-4">
              <li className="flex justify-between items-center text-sm">
                <span className="text-gray-300">URL Transformer</span>
                <span className="text-success flex items-center"><div className="w-2 h-2 rounded-full bg-success mr-2"></div> ONLINE</span>
              </li>
              <li className="flex justify-between items-center text-sm">
                <span className="text-gray-300">Prompt Classifier</span>
                <span className="text-success flex items-center"><div className="w-2 h-2 rounded-full bg-success mr-2"></div> ONLINE</span>
              </li>
              <li className="flex justify-between items-center text-sm">
                <span className="text-gray-300">LLM Analyzer</span>
                <span className="text-success flex items-center"><div className="w-2 h-2 rounded-full bg-success mr-2"></div> ONLINE</span>
              </li>
              <li className="flex justify-between items-center text-sm">
                <span className="text-gray-300">Rust Core</span>
                <span className="text-success flex items-center"><div className="w-2 h-2 rounded-full bg-success mr-2"></div> ONLINE</span>
              </li>
            </ul>
          </div>
        </aside>
      </div>

      <section className="bg-gray-950 p-4 rounded-lg border border-gray-800 font-mono text-sm text-gray-300">
        <div className="flex items-center text-gray-500 mb-2 border-b border-gray-800 pb-2">
          <Terminal className="w-4 h-4 mr-2"/>
          <span>EVENT STREAM</span>
        </div>
        <div className="space-y-1">
          <p><span className="text-blue-400">[INFO]</span> 23:15:02 - New connection from 192.168.1.45</p>
          <p><span className="text-success">[PASS]</span> 23:15:03 - Prompt verified: LOW RISK (Transformer: 98% safe)</p>
          <p><span className="text-warning">[WARN]</span> 23:15:10 - URL anomaly detected on example.com</p>
          <p><span className="text-danger">[BLOCK]</span> 23:15:12 - Blocked prompt injection attempt (Confidence: 95%)</p>
        </div>
      </section>
    </main>
  );
}
