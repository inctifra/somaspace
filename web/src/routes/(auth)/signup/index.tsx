import { createFileRoute } from '@tanstack/react-router'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { useTRPC } from '#/integrations/trpc/react'
import { useMutation } from '@tanstack/react-query'

export const Route = createFileRoute('/(auth)/signup/')({
  component: RouteComponent,
})

const formSchema = z.object({
  email: z.email(),
  password: z.string().min(6),
})

function RouteComponent() {
  const trpc = useTRPC()
  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: '',
      password: '',
    },
  })

  const registerMutation = useMutation(trpc.auth.register.mutationOptions())

  function onSubmit(values: any) {
    console.log(values)
    registerMutation.mutate(values, {
      onSuccess(data) {
        console.log('User registered:', data);
        
      },
      onError(err) {
        console.error('Registration failed:', err)
      },
    })
  }

  return (
    <section className="w-full max-w-md mx-auto py-10 px-4">
      <h1 className="text-2xl font-semibold mb-6">Create an account</h1>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input placeholder="you@email.com" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <Button className="w-full" type="submit">
            Sign up
          </Button>
        </form>
      </Form>
    </section>
  )
}
