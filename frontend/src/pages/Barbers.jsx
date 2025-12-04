import { useState } from 'react'
import { ChevronDown, ChevronUp } from 'lucide-react'
import { useBarbers, useShopInfo } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'
import LoadingSpinner from '../components/LoadingSpinner'
import ErrorMessage from '../components/ErrorMessage'

function Barbers() {
  const { data: barbers, loading, error } = useBarbers()
  const { data: shopInfo } = useShopInfo()
  const [expandedBio, setExpandedBio] = useState(null)

  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL

  const toggleBio = (barberId) => {
    setExpandedBio(expandedBio === barberId ? null : barberId)
  }

  if (loading) return <LoadingSpinner />
  if (error) return <ErrorMessage message={error} />

  return (
    <div className="pt-24 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="section-title">Meet Our Barbers</h1>
          <p className="section-subtitle mx-auto">
            Expert stylists dedicated to making you look your best.
          </p>
        </div>

        {/* Barbers Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {barbers?.map((barber) => (
            <div key={barber.id} className="card p-0 group overflow-hidden border-none bg-transparent rounded-2xl">
              {/* Image */}
              <div className="aspect-[4/5] overflow-hidden relative rounded-2xl">
                {barber.image_url ? (
                  <img
                    src={barber.image_url}
                    alt={barber.name}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 grayscale group-hover:grayscale-0"
                  />
                ) : (
                  <div className="w-full h-full bg-neutral-900 flex items-center justify-center">
                    <span className="text-8xl text-neutral-800 font-display">
                      {barber.name.charAt(0)}
                    </span>
                  </div>
                )}
                <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/0 to-transparent opacity-80"></div>
                
                <div className="absolute bottom-0 left-0 right-0 p-6 translate-y-2 group-hover:translate-y-0 transition-transform duration-500">
                  <h3 className="text-2xl font-bold text-brand-white mb-2 font-display uppercase tracking-wide">
                    {barber.name}
                  </h3>
                  
                  {barber.specialties_list?.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-4">
                      {barber.specialties_list.map((specialty, index) => (
                        <span
                          key={index}
                          className="text-neutral-400 text-xs uppercase tracking-wider"
                        >
                          {specialty}
                          {index < barber.specialties_list.length - 1 && <span className="mx-2 text-neutral-600">•</span>}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              </div>

              {/* Info */}
              <div className="pt-6">
                {barber.bio && (
                  <div className="mb-6">
                    <p className={`text-neutral-500 text-sm font-light leading-relaxed whitespace-pre-line ${
                      expandedBio === barber.id ? '' : 'line-clamp-3'
                    }`}>
                      {barber.bio}
                    </p>
                    {barber.bio.length > 150 && (
                      <button
                        onClick={() => toggleBio(barber.id)}
                        className="flex items-center gap-1 text-neutral-400 hover:text-white text-xs mt-2 transition-colors"
                      >
                        {expandedBio === barber.id ? (
                          <>
                            <span>Show less</span>
                            <ChevronUp className="w-4 h-4" />
                          </>
                        ) : (
                          <>
                            <span>Read more</span>
                            <ChevronDown className="w-4 h-4" />
                          </>
                        )}
                      </button>
                    )}
                  </div>
                )}

                <a
                  href={freshaUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-outline w-full text-center text-xs"
                >
                  Book with {barber.name.split(' ')[0]}
                </a>
              </div>
            </div>
          ))}
        </div>

        {/* Empty State */}
        {barbers?.length === 0 && (
          <div className="text-center py-12">
            <p className="text-neutral-400">No barbers found.</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default Barbers
