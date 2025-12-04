import { AlertCircle } from 'lucide-react'

function ErrorMessage({ message = 'Something went wrong' }) {
  return (
    <div className="flex items-center justify-center py-12">
      <div className="flex items-center space-x-2 text-red-400">
        <AlertCircle className="h-5 w-5" />
        <span>{message}</span>
      </div>
    </div>
  )
}

export default ErrorMessage
