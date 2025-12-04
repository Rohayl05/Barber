import { Link } from 'react-router-dom'
import { Scissors, Phone, Mail, MapPin, Instagram, Facebook } from 'lucide-react'
import { useShopInfo } from '../api/hooks'

function Footer() {
  const { data: shopInfo } = useShopInfo()
  const hours = shopInfo?.opening_hours_parsed || {}

  return (
    <footer className="bg-brand-black border-t border-neutral-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12">
          {/* Brand */}
          <div className="space-y-6">
            <Link to="/" className="flex items-center space-x-2 group">
              <Scissors className="h-6 w-6 text-brand-white group-hover:text-neutral-300 transition-colors" />
              <span className="font-display text-xl font-bold text-brand-white tracking-widest">
                {shopInfo?.shop_name || 'STAYFADED'}
              </span>
            </Link>
            <p className="text-neutral-500 text-sm font-light leading-relaxed">
              {shopInfo?.tagline || 'Premium grooming experience for the modern gentleman.'}
            </p>
            <div className="flex space-x-6">
              {shopInfo?.instagram && (
                <a
                  href={shopInfo.instagram}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-neutral-500 hover:text-brand-white transition-colors"
                >
                  <Instagram className="h-5 w-5" />
                </a>
              )}
              {shopInfo?.facebook && (
                <a
                  href={shopInfo.facebook}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-neutral-500 hover:text-brand-white transition-colors"
                >
                  <Facebook className="h-5 w-5" />
                </a>
              )}
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-bold text-brand-white mb-6 uppercase tracking-widest text-sm">Explore</h4>
            <ul className="space-y-4">
              {['Services', 'Barbers', 'Gallery', 'Contact'].map((item) => (
                <li key={item}>
                  <Link
                    to={`/${item.toLowerCase()}`}
                    className="text-neutral-500 hover:text-brand-white text-sm transition-colors uppercase tracking-wider"
                  >
                    {item}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-bold text-brand-white mb-6 uppercase tracking-widest text-sm">Contact</h4>
            <ul className="space-y-4">
              {shopInfo?.phone && (
                <li className="flex items-center space-x-3 text-neutral-500 text-sm group">
                  <Phone className="h-4 w-4 group-hover:text-brand-white transition-colors" />
                  <a href={`tel:${shopInfo.phone}`} className="hover:text-brand-white transition-colors">
                    {shopInfo.phone}
                  </a>
                </li>
              )}
              {shopInfo?.email && (
                <li className="flex items-center space-x-3 text-neutral-500 text-sm group">
                  <Mail className="h-4 w-4 group-hover:text-brand-white transition-colors" />
                  <a href={`mailto:${shopInfo.email}`} className="hover:text-brand-white transition-colors">
                    {shopInfo.email}
                  </a>
                </li>
              )}
              {shopInfo?.address && (
                <li className="flex items-start space-x-3 text-neutral-500 text-sm group">
                  <MapPin className="h-4 w-4 mt-1 flex-shrink-0 group-hover:text-brand-white transition-colors" />
                  <span>{shopInfo.address}</span>
                </li>
              )}
            </ul>
          </div>

          {/* Opening Hours */}
          <div>
            <h4 className="font-bold text-brand-white mb-6 uppercase tracking-widest text-sm">Hours</h4>
            <ul className="space-y-2 text-sm">
              {Object.entries(hours).map(([day, time]) => (
                <li key={day} className="flex justify-between items-center">
                  <span className="text-neutral-500 capitalize">{day}</span>
                  <span className="text-neutral-300">{time}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-16 pt-8 border-t border-neutral-900 text-center">
          <p className="text-neutral-600 text-sm font-light">
            &copy; {new Date().getFullYear()} {shopInfo?.shop_name || 'StayFaded'}. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
