"use client";
import React from "react";
import { Button } from "../components/ui/button";
import { Sparkles } from "lucide-react";

const Hero = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-background to-slate-900/20 flex items-center justify-center relative overflow-hidden">
      {/* Background gradient effects */}
      <div className="absolute inset-0 bg-gradient-radial from-blue-900/20 via-transparent to-transparent"></div>
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl"></div>
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl"></div>

      <div className="relative z-10 text-center max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Beta badge */}
        <div className="mb-8 animate-fade-in">
          <div className="inline-flex items-center px-4 py-2 rounded-full border border-blue-500/30 bg-blue-500/10 text-blue-300 text-sm font-medium">
            <span>By Parth Sohaney</span>
            <Sparkles className="ml-2 h-4 w-4" />
          </div>
        </div>

        {/* Tagline */}
        <div
          className="mb-8 animate-fade-in"
          style={{ animationDelay: "0.1s" }}
        >
          <p className="text-muted-foreground text-lg">
            For{" "}
            <span className="text-blue-400  cursor-pointer hover:text-blue-300 transition-colors">
              Traders
            </span>{" "}
            by a Developer
          </p>
        </div>

        {/* Main heading */}
        <div
          className="mb-8 animate-fade-in"
          style={{ animationDelay: "0.2s" }}
        >
          <h1 className="text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold leading-tight tracking-tight">
            <span className="text-white">Analyze the market</span>
            <br />
            <span className="text-white">in minutes with </span>
            <br />
            <span className="bg-gradient-to-r from-gray-400 to-gray-600 bg-clip-text text-transparent">
              Trade_Peeps
            </span>
          </h1>
        </div>

        {/* Description */}
        <div
          className="mb-12 animate-fade-in"
          style={{ animationDelay: "0.3s" }}
        >
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            Get real-time trade insights and expert analysis from
            SEBI-registered professionals.
            <br />
            Join thousands of investors making informed decisions today.
          </p>
        </div>

        {/* CTA Buttons */}
        <div
          className="flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-in"
          style={{ animationDelay: "0.4s" }}
        >
          <a href="/bulk-deals">
            <Button
              size="lg"
              className="bg-white text-black hover:bg-gray-200 text-lg px-8 py-3 h-auto font-medium transition-all duration-200 hover:scale-105"
            >
              Get started
            </Button>
          </a>

          <Button
            variant="outline"
            size="lg"
            className="border-gray-600 text-gray-300 hover:bg-gray-800 hover:text-white text-lg px-8 py-3 h-auto font-medium transition-all duration-200 hover:scale-105"
            onClick={() =>
              window.open(
                "https://github.com/Pa04rth/Trading_Peeps#readme",
                "_blank"
              )
            }
          >
            Documentation
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Hero;
