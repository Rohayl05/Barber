import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true,
    allowedHosts: [
      'plashier-regenia-consciously.ngrok-free.dev',
      '.ngrok-free.dev',
      'localhost',
      '127.0.0.1'
    ],
    hmr: {
      host: 'plashier-regenia-consciously.ngrok-free.dev',
      protocol: 'wss'
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: false
  }
})
