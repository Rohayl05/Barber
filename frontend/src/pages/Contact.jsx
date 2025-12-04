import { Phone, Mail, MapPin, Clock, MessageCircle } from 'lucide-react'
import { useShopInfo } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'
import LoadingSpinner from '../components/LoadingSpinner'

function Contact() {
  const { data: shopInfo, loading } = useShopInfo()
  const hours = shopInfo?.opening_hours_parsed || {}
  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL

  if (loading) return <LoadingSpinner />

  return (
    <div className="pt-24 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="section-title">Contact Us</h1>
          <p className="section-subtitle mx-auto">
            Get in touch or visit us at our shop.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          {/* Contact Info */}
          <div className="space-y-8">
            {/* Contact Details */}
            <div className="card p-6">
              <h2 className="text-xl font-semibold text-white mb-6">Get in Touch</h2>
              <div className="space-y-4">
                {shopInfo?.phone && (
                  <a
                    href={`tel:${shopInfo.phone}`}
                    className="flex items-center space-x-4 text-neutral-300 hover:text-accent transition-colors group"
                  >
                    <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center group-hover:bg-accent/20 transition-colors">
                      <Phone className="h-5 w-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-neutral-500">Phone</p>
                      <p className="font-medium">{shopInfo.phone}</p>
                    </div>
                  </a>
                )}

                {shopInfo?.whatsapp && (
                  <a
                    href={`https://wa.me/${shopInfo.whatsapp.replace(/\D/g, '')}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center space-x-4 text-neutral-300 hover:text-accent transition-colors group"
                  >
                    <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center group-hover:bg-accent/20 transition-colors">
                      <MessageCircle className="h-5 w-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-neutral-500">WhatsApp</p>
                      <p className="font-medium">{shopInfo.whatsapp}</p>
                    </div>
                  </a>
                )}

                {shopInfo?.email && (
                  <a
                    href={`mailto:${shopInfo.email}`}
                    className="flex items-center space-x-4 text-neutral-300 hover:text-accent transition-colors group"
                  >
                    <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center group-hover:bg-accent/20 transition-colors">
                      <Mail className="h-5 w-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-neutral-500">Email</p>
                      <p className="font-medium">{shopInfo.email}</p>
                    </div>
                  </a>
                )}

                {shopInfo?.address && (
                  <div className="flex items-start space-x-4 text-neutral-300">
                    <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center flex-shrink-0">
                      <MapPin className="h-5 w-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-neutral-500">Address</p>
                      <p className="font-medium whitespace-pre-line">{shopInfo.address}</p>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Opening Hours */}
            <div className="card p-6">
              <div className="flex items-center space-x-2 mb-6">
                <Clock className="h-5 w-5 text-accent" />
                <h2 className="text-xl font-semibold text-white">Opening Hours</h2>
              </div>
              <div className="space-y-3">
                {Object.entries(hours).map(([day, time]) => (
                  <div
                    key={day}
                    className="flex justify-between items-center py-2 border-b border-neutral-800 last:border-0"
                  >
                    <span className="text-neutral-300 capitalize">{day}</span>
                    <span className={`font-medium ${time === 'Closed' ? 'text-red-400' : 'text-accent'}`}>
                      {time}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Book Button */}
            <a
              href={freshaUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary w-full text-center text-lg py-4"
            >
              Book an Appointment
            </a>
          </div>

          {/* Map */}
          <div className="card overflow-hidden h-[500px] lg:h-auto">
            {shopInfo?.google_maps_embed ? (
              <div 
                className="w-full h-full min-h-[400px]"
                dangerouslySetInnerHTML={{ __html: shopInfo.google_maps_embed }}
              />
            ) : (
              <div className="w-full h-full min-h-[400px] bg-neutral-800 flex items-center justify-center">
                <div className="text-center text-neutral-500">
                  <MapPin className="h-12 w-12 mx-auto mb-4" />
                  <p>Map will be displayed here</p>
                  <p className="text-sm mt-2">Add Google Maps embed code in admin</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Contact
