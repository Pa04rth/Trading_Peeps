"use client";

import { useEffect, useState } from "react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { Zap, Package, TrendingUp, Clock, LandPlot } from "lucide-react";
import { get } from "http";

const Blogs = () => {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-20 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center space-x-2 bg-secondary/50 px-4 py-2 rounded-full mb-6">
            <Zap className="h-4 w-4 text-blue-400" />
            <span className="text-sm text-muted-foreground">Route : /blog</span>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-white via-gray-200 to-gray-400 bg-clip-text text-transparent">
            Blogs
          </h1>

          <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto">
            Blogs will be available soon. Stay tuned for updates on the latest
            trends, insights, and analyses in the world of finance and trading.
          </p>

          <div className="flex flex-wrap justify-center gap-4 mb-12">
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <LandPlot className="h-5 w-5 text-blue-400" />
              <span className="text-sm">Blogs</span>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Blogs;
