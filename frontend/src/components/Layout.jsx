import Navbar from './Navbar'
import Footer from './Footer'
import BookingCTA from './BookingCTA'

function Layout({ children }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow">
        {children}
      </main>
      <BookingCTA />
      <Footer />
    </div>
  )
}

export default Layout
