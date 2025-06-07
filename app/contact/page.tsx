"use client";

import { useEffect, useState } from "react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import {
  Zap,
  Package,
  TrendingUp,
  Clock,
  LandPlot,
  X,
  Facebook,
  Instagram,
  FacebookIcon,
  InstagramIcon,
  Linkedin,
} from "lucide-react";
import { get } from "http";

const Contact = () => {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-20 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center space-x-2 bg-secondary/50 px-4 py-2 rounded-full mb-6">
            <Zap className="h-4 w-4 text-blue-400" />
            <span className="text-sm text-muted-foreground">
              Route : /contact
            </span>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-white via-gray-200 to-gray-400 bg-clip-text text-transparent">
            Contact Us
          </h1>

          <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto">
            Stay in touch using the following links..
          </p>

          <div className="flex flex-wrap justify-center gap-4 mb-12">
            <a href="https://www.x.com/tradepeeps">
              <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
                <X className="h-5 w-5 text-blue-400" />
                <span className="text-sm">Twitter</span>
              </div>
            </a>
            <a href="https://www.linkedin.com/company/tradepeeps">
              <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
                <Linkedin className="h-5 w-5 text-green-400" />
                <span className="text-sm">LinkedIn</span>
              </div>
            </a>

            <a href="https://www.instagram.com/tradepeeps">
              <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
                <InstagramIcon className="h-5 w-5 text-orange-400" />
                <span className="text-sm">Instagram</span>
              </div>
            </a>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Contact;
