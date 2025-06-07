"use client";

import { useEffect, useState } from "react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { Zap, Package, TrendingUp, Clock } from "lucide-react";
import { get } from "http";

type Deal = {
  buy_sell: string;
  buyer: string;
  company_name: string;
  deal_date: string;
  deal_volume: number;
  is_hft_filtered: boolean;
  price: number;
  remarks: string;
  symbol: string;
  volume_percentage: number;
};

const BulkDeals = () => {
  const [deals, setDeals] = useState<Deal[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDeals = async () => {
      try {
        const response = await fetch("/api/bulk-deals", { method: "GET" });
        const data = await response.json();
        setDeals(data.deals || []);
      } catch (error) {
        console.error("Error fetching bulk deals:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDeals();
  }, []);

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-20 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center space-x-2 bg-secondary/50 px-4 py-2 rounded-full mb-6">
            <Zap className="h-4 w-4 text-blue-400" />
            <span className="text-sm text-muted-foreground">
              API : /api/bulk-deal
            </span>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-white via-gray-200 to-gray-400 bg-clip-text text-transparent">
            Bulk Deals Report
          </h1>

          <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto">
            View bulk deals with buy/sell indicators and HFT filters.
          </p>

          <div className="flex flex-wrap justify-center gap-4 mb-12">
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <Package className="h-5 w-5 text-blue-400" />
              <span className="text-sm">Symbols</span>
            </div>
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <TrendingUp className="h-5 w-5 text-green-400" />
              <span className="text-sm">Volume %</span>
            </div>
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <Clock className="h-5 w-5 text-orange-400" />
              <span className="text-sm">Time Range</span>
            </div>
          </div>
        </div>
      </section>

      {/* Table Section */}
      <section className="px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto mb-16">
        {loading ? (
          <p className="text-center text-muted-foreground">Loading deals...</p>
        ) : (
          <div className="overflow-auto rounded-lg shadow border border-border">
            <table className="min-w-full divide-y divide-border">
              <thead className="bg-muted text-left">
                <tr>
                  <th className="px-4 py-3 text-sm font-semibold">Symbol</th>
                  <th className="px-4 py-3 text-sm font-semibold">Company</th>
                  <th className="px-4 py-3 text-sm font-semibold">Buyer</th>
                  <th className="px-4 py-3 text-sm font-semibold">Buy/Sell</th>
                  <th className="px-4 py-3 text-sm font-semibold">Volume</th>
                  <th className="px-4 py-3 text-sm font-semibold">Price</th>
                  <th className="px-4 py-3 text-sm font-semibold">Date</th>
                </tr>
              </thead>
              <tbody className="bg-background divide-y divide-border">
                {deals.map((deal, idx) => (
                  <tr key={idx}>
                    <td className="px-4 py-2 text-sm">{deal.symbol}</td>
                    <td className="px-4 py-2 text-sm">{deal.company_name}</td>
                    <td className="px-4 py-2 text-sm">{deal.buyer}</td>
                    <td className="px-4 py-2 text-sm">{deal.buy_sell}</td>
                    <td className="px-4 py-2 text-sm">{deal.price}</td>
                    <td className="px-4 py-2 text-sm">{deal.deal_date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <Footer />
    </div>
  );
};

export default BulkDeals;
