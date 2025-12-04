import { Calendar } from 'lucide-react'
import { useShopInfo } from '../api/hooks'
import { DEFAULT_FRESHA_URL } from '../api/config'

function BookingCTA() {
  const { data: shopInfo } = useShopInfo()
  const freshaUrl = shopInfo?.fresha_url || DEFAULT_FRESHA_URL

  return (
    <section className="bg-brand-white py-20">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 className="font-display text-3xl md:text-4xl font-bold text-black mb-6 tracking-tight">
          Ready for a Fresh Look?
        </h2>
        <p className="text-neutral-600 mb-10 max-w-xl mx-auto font-light text-lg">
          Book your appointment today and experience premium grooming at its finest.
        </p>
        <a
          href={freshaUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center justify-center px-10 py-4 bg-black hover:bg-neutral-800 text-white font-semibold rounded-full transition-all duration-300 tracking-wide uppercase text-sm space-x-3"
        >
          <Calendar className="h-5 w-5" />
          <span>Book Appointment</span>
        </a>
      </div>
    </section>
  )
}

export default BookingCTA
