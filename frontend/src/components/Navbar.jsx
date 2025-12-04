import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Menu, X, Scissors } from 'lucide-react'
import { useShopInfo } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'

function Navbar() {
  const [isOpen, setIsOpen] = useState(false)
  const location = useLocation()
  const { data: shopInfo } = useShopInfo()
  
  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL

  const navLinks = [
    { path: '/', label: 'Home' },
    { path: '/services', label: 'Services' },
    { path: '/barbers', label: 'Barbers' },
    { path: '/gallery', label: 'Gallery' },
    { path: '/contact', label: 'Contact' },
  ]

  const isActive = (path) => location.pathname === path

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-neutral-950/95 backdrop-blur-sm border-b border-neutral-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2 group">
            <Scissors className="h-8 w-8 text-brand-white group-hover:text-neutral-300 transition-colors" />
            <span className="font-display text-xl font-bold text-brand-white tracking-wider">
              {shopInfo?.shop_name || 'STAYFADED'}
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`text-sm uppercase tracking-widest transition-colors ${
                  isActive(link.path)
                    ? 'text-brand-white font-semibold'
                    : 'text-neutral-400 hover:text-brand-white'
                }`}
              >
                {link.label}
              </Link>
            ))}
            <a
              href={freshaUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary"
            >
              Book Now
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 text-brand-white hover:text-neutral-300"
          >
            {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden py-4 border-t border-neutral-800 bg-brand-black">
            <div className="flex flex-col space-y-4">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  onClick={() => setIsOpen(false)}
                  className={`text-sm uppercase tracking-widest px-4 py-3 transition-colors ${
                    isActive(link.path)
                      ? 'text-brand-white bg-neutral-900'
                      : 'text-neutral-400 hover:text-brand-white hover:bg-neutral-900'
                  }`}
                >
                  {link.label}
                </Link>
              ))}
              <div className="px-4 pt-2">
                <a
                  href={freshaUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-primary w-full text-center"
                >
                  Book Now
                </a>
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}

export default Navbar
