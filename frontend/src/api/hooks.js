import { useState, useEffect } from 'react'
import { API_BASE_URL } from './config'

/**
 * Generic fetch hook for API calls
 */
function useFetch(endpoint) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true)
        const response = await fetch(`${API_BASE_URL}${endpoint}`)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const json = await response.json()
        // Handle paginated responses
        setData(json.results || json)
        setError(null)
      } catch (err) {
        console.error(`Error fetching ${endpoint}:`, err)
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [endpoint])

  return { data, loading, error }
}

/**
 * Fetch services from API
 */
export function useServices(category = null) {
  const endpoint = category ? `/services/?category=${category}` : '/services/'
  return useFetch(endpoint)
}

/**
 * Fetch barbers from API
 */
export function useBarbers() {
  return useFetch('/barbers/')
}

/**
 * Fetch gallery images from API
 */
export function useGallery(category = null) {
  const endpoint = category ? `/gallery/?category=${category}` : '/gallery/'
  return useFetch(endpoint)
}

/**
 * Fetch shop information from API
 */
export function useShopInfo() {
  return useFetch('/shop-info/')
}
