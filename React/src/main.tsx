import { createRoot } from 'react-dom/client'
import './index.css'
import { Layout } from './Components/LayoutArea/Layout/Layout'
import { BrowserRouter } from 'react-router-dom'
import { Toaster } from 'react-hot-toast'

createRoot(document.getElementById('root')!).render(
    <BrowserRouter>
        <Toaster />
        <Layout />
    </BrowserRouter>
)
