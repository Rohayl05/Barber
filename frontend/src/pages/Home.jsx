import { Link } from 'react-router-dom'
import { ArrowRight, Clock, Star, Users } from 'lucide-react'
import { useShopInfo, useServices, useGallery } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'
import LoadingSpinner from '../components/LoadingSpinner'

function Home() {
  const { data: shopInfo, loading: shopLoading } = useShopInfo()
  const { data: services } = useServices()
  const { data: gallery } = useGallery()

  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL
  const hours = shopInfo?.opening_hours_parsed || {}
  const previewImages = gallery?.slice(0, 6) || []
  const featuredServices = services?.slice(0, 4) || []

  return (
    <div>
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center pt-16">
        <div 
          className="absolute inset-0 bg-cover bg-center bg-no-repeat"
          style={{
            backgroundImage: shopInfo?.hero_image_url 
              ? `url(${shopInfo.hero_image_url})`
              : 'url(https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=2074&auto=format&fit=crop)'
          }}
        >
          <div className="absolute inset-0 bg-black/80"></div>
        </div>
        
        <div className="relative z-10 max-w-4xl mx-auto px-4 text-center">
          <h1 className="font-display text-4xl md:text-6xl lg:text-7xl font-bold text-brand-white mb-6 tracking-tight">
            {shopInfo?.hero_title || 'PRECISION & STYLE'}
          </h1>
          <p className="text-xl md:text-2xl text-neutral-300 mb-10 max-w-2xl mx-auto font-light">
            {shopInfo?.hero_subtitle || 'Fresh fades, clean cuts, and modern styles.'}
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a
              href={freshaUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary text-lg px-10 py-4"
            >
              Book Appointment
            </a>
            <Link to="/services" className="btn-outline text-lg px-10 py-4">
              View Services
            </Link>
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
          <div className="w-6 h-10 rounded-full border border-white/30 flex items-start justify-center p-2">
            <div className="w-1 h-2 bg-white rounded-full animate-pulse"></div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-brand-dark border-y border-neutral-900 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {[
              { icon: Users, label: 'Happy Clients', value: '5000+' },
              { icon: Star, label: 'Years Experience', value: '10+' },
              { icon: Clock, label: 'Cuts Per Day', value: '50+' },
              { icon: Star, label: '5-Star Reviews', value: '500+' },
            ].map((stat, index) => (
              <div key={index} className="text-center">
                <stat.icon className="h-6 w-6 text-brand-white mx-auto mb-4 opacity-80" />
                <div className="font-display text-3xl font-bold text-brand-white mb-1">
                  {stat.value}
                </div>
                <div className="text-neutral-500 text-xs uppercase tracking-widest">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Preview */}
      <section className="py-20 bg-brand-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="section-title">SERVICES</h2>
            <p className="section-subtitle mx-auto">
              Tailored grooming for the modern gentleman.
            </p>
          </div>

          {shopLoading ? (
            <LoadingSpinner />
          ) : (
            <>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {featuredServices.map((service) => (
                  <div key={service.id} className="card group hover:bg-neutral-900">
                    <h3 className="font-bold text-brand-white text-lg mb-2 uppercase tracking-wide">
                      {service.title}
                    </h3>
                    <p className="text-neutral-500 text-sm mb-6 line-clamp-2">
                      {service.description || `${service.duration_minutes} minutes`}
                    </p>
                    <div className="flex items-center justify-between mt-auto">
                      <span className="text-brand-white font-bold text-xl">
                        ${service.price}
                      </span>
                      <span className="text-neutral-600 text-xs uppercase tracking-wider border border-neutral-800 px-2 py-1 rounded-md">
                        {service.duration_minutes} min
                      </span>
                    </div>
                  </div>
                ))}
              </div>
              
              <div className="text-center mt-16">
                <Link to="/services" className="btn-outline inline-flex items-center space-x-2 px-8">
                  <span>View All Services</span>
                  <ArrowRight className="h-4 w-4 ml-2" />
                </Link>
              </div>
            </>
          )}
        </div>
      </section>

      {/* Gallery Preview */}
      {previewImages.length > 0 && (
        <section className="py-20 bg-neutral-900">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="section-title">Our Work</h2>
              <p className="section-subtitle mx-auto">
                Check out some of our recent cuts and styles.
              </p>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              {previewImages.map((image) => (
                <div
                  key={image.id}
                  className="aspect-square rounded-lg overflow-hidden group"
                >
                  <img
                    src={image.image_url}
                    alt={image.alt_text || image.title || 'Gallery image'}
                    className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                  />
                </div>
              ))}
            </div>

            <div className="text-center mt-10">
              <Link to="/gallery" className="btn-outline inline-flex items-center space-x-2">
                <span>View Full Gallery</span>
                <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </div>
        </section>
      )}

      {/* Opening Hours */}
      <section className="py-20 bg-brand-black border-t border-neutral-900">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="section-title">OPENING HOURS</h2>
          </div>

          <div className="card bg-brand-dark p-8 md:p-12">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-4">
              {Object.entries(hours).map(([day, time]) => (
                <div
                  key={day}
                  className="flex justify-between items-center py-4 border-b border-neutral-800/50 last:border-0"
                >
                  <span className="text-neutral-400 uppercase tracking-wider text-sm font-medium">{day}</span>
                  <span className={`${time === 'Closed' ? 'text-neutral-600' : 'text-brand-white'} font-medium`}>
                    {time}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Home
