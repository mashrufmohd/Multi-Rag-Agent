import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Brain, FileText, Sparkles, PenTool } from "lucide-react"
import Link from "next/link"

export default function Home() {
  const features = [
    {
      icon: <Brain className="h-8 w-8" />,
      title: "Text Summarization",
      description: "Condense long texts into clear, concise summaries",
      href: "/summarize"
    },
    {
      icon: <Sparkles className="h-8 w-8" />,
      title: "Text Sanitization",
      description: "Clean and format text for professional use",
      href: "/sanitize"
    },
    {
      icon: <PenTool className="h-8 w-8" />,
      title: "Article Writing",
      description: "Generate high-quality articles with AI assistance",
      href: "/write_article"
    },
    {
      icon: <FileText className="h-8 w-8" />,
      title: "Text Analysis",
      description: "Get insights and statistics about your text",
      href: "/analyze"
    }
  ]

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold tracking-tight mb-4">
          AI-Powered Text Processing
        </h1>
        <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
          Transform your text with advanced AI technology. Summarize, sanitize, and generate content
          with professional-grade tools.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
        {features.map((feature) => (
          <Link key={feature.title} href={feature.href}>
            <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
              <CardHeader>
                <div className="mb-4 text-primary">
                  {feature.icon}
                </div>
                <CardTitle>{feature.title}</CardTitle>
                <CardDescription>{feature.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="text-sm text-muted-foreground">
                  Click to get started →
                </div>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  )
}