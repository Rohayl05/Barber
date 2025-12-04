import { useState, useMemo } from 'react'
import { Clock, DollarSign } from 'lucide-react'
import { useServices, useShopInfo } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'
import LoadingSpinner from '../components/LoadingSpinner'
import ErrorMessage from '../components/ErrorMessage'

function Services() {
  const { data: services, loading, error } = useServices()
  const { data: shopInfo } = useShopInfo()
  const [activeCategory, setActiveCategory] = useState('all')

  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL

  // Get unique categories from services
  const categories = useMemo(() => {
    if (!services) return []
    const cats = [...new Set(services.map((s) => s.category).filter(Boolean))]
    return ['all', ...cats]
  }, [services])

  // Filter services by category
  const filteredServices = useMemo(() => {
    if (!services) return []
    if (activeCategory === 'all') return services
    return services.filter((s) => s.category === activeCategory)
  }, [services, activeCategory])

  // Group services by category
  const groupedServices = useMemo(() => {
    if (activeCategory !== 'all') {
      return { [activeCategory]: filteredServices }
    }
    return filteredServices.reduce((acc, service) => {
      const cat = service.category || 'Other'
      if (!acc[cat]) acc[cat] = []
      acc[cat].push(service)
      return acc
    }, {})
  }, [filteredServices, activeCategory])

  if (loading) return <LoadingSpinner />
  if (error) return <ErrorMessage message={error} />

  return (
    <div className="pt-24 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="section-title">Our Services</h1>
          <p className="section-subtitle mx-auto">
            Professional grooming services tailored to your style.
          </p>
        </div>

        {/* Category Filter */}
        {categories.length > 1 && (
          <div className="flex flex-wrap justify-center gap-4 mb-16">
            {categories.map((category) => (
              <button
                key={category}
                onClick={() => setActiveCategory(category)}
                className={`px-6 py-2 text-sm font-semibold uppercase tracking-wider transition-all border rounded-full ${
                  activeCategory === category
                    ? 'bg-brand-white text-black border-brand-white'
                    : 'bg-transparent text-neutral-400 border-neutral-800 hover:border-neutral-500 hover:text-brand-white'
                }`}
              >
                {category === 'all' ? 'All Services' : category}
              </button>
            ))}
          </div>
        )}

        {/* Services List */}
        <div className="space-y-20">
          {Object.entries(groupedServices).map(([category, categoryServices]) => (
            <div key={category}>
              {activeCategory === 'all' && (
                <h2 className="text-2xl font-display font-bold text-brand-white mb-8 capitalize tracking-wide border-l-4 border-brand-white pl-4">
                  {category}
                </h2>
              )}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {categoryServices.map((service) => (
                  <div key={service.id} className="card flex flex-col group hover:bg-neutral-900 hover:border-neutral-600">
                    <div className="flex-grow">
                      <h3 className="text-xl font-bold text-brand-white mb-3 uppercase tracking-wide">
                        {service.title}
                      </h3>
                      {service.description && (
                        <p className="text-neutral-500 text-sm mb-6 font-light leading-relaxed">
                          {service.description}
                        </p>
                      )}
                    </div>
                    
                    <div className="flex items-center justify-between pt-6 border-t border-neutral-800/50 group-hover:border-neutral-700">
                      <div className="flex items-center space-x-4">
                        <div className="flex items-center text-brand-white">
                          <span className="font-bold text-xl">${service.price}</span>
                        </div>
                        <div className="flex items-center text-neutral-500 text-xs uppercase tracking-widest">
                          <Clock className="h-3 w-3 mr-1" />
                          <span>{service.duration_minutes} min</span>
                        </div>
                      </div>
                      <a
                        href={freshaUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-brand-white hover:text-neutral-300 text-sm font-semibold uppercase tracking-wider transition-colors"
                      >
                        Book
                      </a>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Empty State */}
        {filteredServices.length === 0 && (
          <div className="text-center py-12">
            <p className="text-neutral-400">No services found.</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default Services
