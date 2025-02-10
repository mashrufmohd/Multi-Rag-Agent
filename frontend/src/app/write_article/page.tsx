"use client"

import { useState } from "react"
import axios from "axios"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { PenTool } from "lucide-react"

export default function WriteArticle() {
  const [topic, setTopic] = useState("")
  const [keywords, setKeywords] = useState("")
  const [outline, setOutline] = useState("")
  const [article, setArticle] = useState("")
  const [refinedArticle, setRefinedArticle] = useState("")
  const [validation, setValidation] = useState("")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  const handleGenerateAndRefine = async () => {
    if (!topic.trim()) {
      setError("Please enter a topic for the article.")
      return
    }

    setLoading(true)
    setError("")
    setArticle("")
    setRefinedArticle("")
    setValidation("")

    try {
      const response = await axios.post("http://127.0.0.1:5000/write-article", { topic, outline, keywords })
      setArticle(response.data.article)
      setRefinedArticle(response.data.refinedArticle)
      setValidation(response.data.validation)
    } catch (error) {
      console.error("Error:", error)
      setError("Failed to generate and refine the article. Please try again.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center gap-4 mb-8">
          <PenTool className="h-8 w-8 text-primary" />
          <div>
            <h1 className="text-3xl font-bold tracking-tight">Article Generator</h1>
            <p className="text-muted-foreground">Create high-quality articles with AI assistance</p>
          </div>
        </div>

        <div className="grid gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Article Parameters</CardTitle>
              <CardDescription>Define your article topic, keywords, and outline</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <label className="text-sm font-medium">Topic</label>
                <Input
                  placeholder="Enter the main topic..."
                  value={topic}
                  onChange={(e) => setTopic(e.target.value)}
                />
              </div>
              <div className="space-y-2">
                <label className="text-sm font-medium">Keywords</label>
                <Input
                  placeholder="Enter keywords (comma separated)..."
                  value={keywords}
                  onChange={(e) => setKeywords(e.target.value)}
                />
              </div>
              <div className="space-y-2">
                <label className="text-sm font-medium">Outline (Optional)</label>
                <Textarea
                  placeholder="Enter article outline..."
                  value={outline}
                  onChange={(e) => setOutline(e.target.value)}
                />
              </div>
            </CardContent>
          </Card>

          <div className="flex justify-center">
            <Button size="lg" onClick={handleGenerateAndRefine} disabled={loading}>
              {loading ? "Writing and Refining..." : "Generate and Refine Article"}
            </Button>
          </div>

          {error && <p className="text-red-500 text-sm mt-2 text-center">{error}</p>}

          {article && (
            <Card>
              <CardHeader>
                <CardTitle>Generated Article</CardTitle>
                <CardDescription>Your AI-generated article will appear here</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="p-4 rounded-lg bg-muted">
                  <h2 className="font-semibold text-gray-800">Draft Article:</h2>
                  <p className="text-gray-700">{article}</p>

                  <h2 className="font-semibold text-gray-800 mt-3">Refined Article:</h2>
                  <p className="text-gray-700">{refinedArticle}</p>

                  <h2 className="font-semibold text-gray-800 mt-3">Validation:</h2>
                  <p className="text-gray-700">{validation}</p>
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  )
}
